"""TODO: Add missing doctring."""

from openfisca_core.periods import MONTH, YEAR
from openfisca_core.variables import Variable

from openfisca_aotearoa.entities import Person


class yearly_income(Variable):
    value_type = float
    entity = Person
    label = u"Yearly income of this person"
    definition_period = YEAR
    reference = u"TODO"
    unit = "NZD"
    set_input = set_input_divide_by_period


class monthly_income(Variable):
    value_type = float
    entity = Person
    label = u"Monthly income of this person"
    definition_period = MONTH
    reference = u"One twelfth of their yearly income"
    unit = "NZD"
