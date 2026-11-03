# Creates the shop, starting with no books and no orders.
#
# STARTING POINT: the shop still uses the layered code from stage 1
# (business.py, persistence.py, presentation.py).
# In step 3 you will build it from the catalog/ and orders/ domains instead.

import persistence
from presentation import ShopAPI
import catalog.presentation as catalog
import orders.presentation as orders
import errors
import orders.business as orders_business
import catalog.business as catalog_business

def create_app():
    persistence.reset()
    return ShopAPI()
