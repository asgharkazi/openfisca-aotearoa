"""TODO: Add missing doctring."""

import os

from openfisca_core.taxbenefitsystems import TaxBenefitSystem

from . import entities

COUNTRY_DIR = os.path.dirname(__file__)


# Our country tax and benefit class inherits from the general TaxBenefitSystem class.
# The name CountryTaxBenefitSystem must not be changed, as all tools of the OpenFisca ecosystem expect a CountryTaxBenefitSystem class to be exposed in the __init__ module of a country package.
class CountryTaxBenefitSystem(TaxBenefitSystem):
    def __init__(self):
        # We initialize our tax and benefit system with the general constructor
        super().__init__(entities.entities)

        # We add to our tax and benefit system all the variables
        self.add_variables_from_directory(os.path.join(COUNTRY_DIR, "variables"))

        # We add to our tax and benefit system all the legislation parameters defined in the  parameters files
        self.load_parameters(os.path.join(COUNTRY_DIR, "parameters"))
