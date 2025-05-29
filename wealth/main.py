from uuid import uuid4

from wealth.core.finance import Finance
from wealth.data.allocations import create_default_allocations
from services.api.logging import setup_logging, log

setup_logging()

# 1. Create your user and Finance system
user_id = str(uuid4())
user_name = "Alan Szmyt"

finance = Finance.default(user_id=user_id, notes=f"{user_name}'s system initialized.")

# 2. Get allocations from data source.
allocations = create_default_allocations(finance=finance)

# 3. Add allocations to the system
finance.add_allocations(allocations)

# 4. Output the result
log.info(finance.to_json(indent=2))

finance.plot_allocation_chart(show=True, save_path="output/allocation_chart.png")
