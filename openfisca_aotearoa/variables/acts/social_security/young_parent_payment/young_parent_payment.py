"""TODO: Add missing doctring."""

from openfisca_core import periods, variables

from openfisca_aotearoa import entities


class young_parent_payment__granted(variables.Variable):
    value_type = bool
    default_value = False
    entity = entities.Person
    label = "Person is currently granted the young parent benefit"
    definition_period = periods.DateUnit.WEEK
    reference = "Reference is unclear, but variable is utilised by the phrase: 'granted a main benefit'"


class young_parent_payment__receiving(variables.Variable):
    value_type = bool
    default_value = False
    entity = entities.Person
    label = "Person is currently recieving/being paid the young parent payment"
    definition_period = periods.DateUnit.WEEK
    reference = "Reference is unclear, but concept underpinning the variable assumes it covers both: 'being paid a main benefit' or 'recieving a benefit'"


# TODO: Review against the new 2018 act
class young_parent_payment__entitled(variables.Variable):
    value_type = bool
    entity = entities.Person
    definition_period = periods.DateUnit.MONTH
    label = "Eligible for Young Parent Payment"
    reference = "http://legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM4686080"
    """

    164 Young parent payment: basic criteria
    (1) The basic qualifications for entitlement to a young parent payment are in subsection (2). The qualifications for a single person are in section 165.
        The qualifications for a young person who is or has been married, in a civil union, or in a de facto relationship are in section 166.

    (2) <--  snip - see young_parent_payment__basic_requirements -->

    (3) Nothing in subsection (2)﻿(e) affects the entitlement of a young person to receive a young parent payment if, during a temporary period, the person
        has income sufficient to fully abate the payment but the person otherwise fulfils the conditions of entitlement to the payment.
    (4) For the purposes of subsection (2)﻿(b), a dependent child of a young person who is married, in a civil union, or in a de facto relationship must
        also be treated as a dependent child of the young person’s spouse or partner.
    """

    def formula(persons, period, parameters):
        basic_requirements = persons(
            "young_parent_payment__basic_requirements", period)

        single_requirements = persons(
            "young_parent_payment__single_young_persons", period)
        in_relationship_requirements = persons(
            "young_parent_payment__relationship_requirements", period)

        # 74AA (2)
        residency = persons(
            "social_security__residential_requirement", period.first_week)

        return basic_requirements * (single_requirements + in_relationship_requirements) * residency


class young_parent_payment__base(variables.Variable):
    value_type = float
    default_value = 0
    entity = entities.Person
    label = "TODO"
    definition_period = periods.DateUnit.WEEK
    reference = "TODO"


# TODO: Review against the new 2018 act
class young_parent_payment__basic_requirements(variables.Variable):
    value_type = bool
    entity = entities.Person
    definition_period = periods.DateUnit.MONTH
    label = "Meets young parent payment basic requirements"
    reference = "http://legislation.govt.nz/act/public/1964/0136/latest/whole.html#DLM4686080"
    """
    (2) The basic qualifications for entitlement to a young parent payment are that the young person
        (a) is aged 16 to 19 years; and
        (b) is a parent or step-parent of a dependent child or dependent children; and
        (c) either
            (i) is undertaking or is available for a full-time course of secondary instruction, tertiary education, approved training, or approved
            work-based learning, leading to
                (A) NCEA level 2; or
                (B) an equivalent qualification (in the opinion of the chief executive); or
                (C) a higher qualification; or
            (ii) would be so available but for circumstances
                (A) under which the obligation to undertake education or training or work-based learning in section 170(1)﻿(a) would not, under
                    section 170(3), apply to the young person; or
                (B) that would qualify the young person for an exemption under section 105 from that obligation; and
        (d) meets the residential requirements set out in section 74AA; and
        (e) has no income or an income of less than the amount that would fully abate the young parent payment.
    """

    def formula(persons, period, parameters):
        # (a) is aged 16 to 19 years; and
        age_test = (persons("age", period.start) >= 16) * \
            (persons("age", period.start) < 20)

        # (b) is a parent or step-parent of a dependent child or dependent children; and
        is_parent_of_dependent_children = (persons("social_security__parent", period) + persons(
            "person_is_step_parent", period)) * (persons("social_security__dependent_children", period.first_week) > 0)

        # (e) has no income or an income of less than the amount that would fully abate the young parent payment.
        income_test = persons(
            "young_parent_payment__income_under_threshold", period)

        return age_test * is_parent_of_dependent_children * income_test


# TODO: Review against the new 2018 act
class young_parent_payment__income_under_threshold(variables.Variable):
    value_type = bool
    entity = entities.Person
    definition_period = periods.DateUnit.MONTH
    label = "Is their income under the Young Parent Payment threshold?"

    def formula(persons, period, parameters):
        yearly_income = (persons("monthly_income", period) * 12)
        yearly_income_threshold = (
            52 * parameters(period).entitlements.social_security.young_parent_payment.weekly_income_threshold)
        return yearly_income < yearly_income_threshold
