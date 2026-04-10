import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'agri_platform.settings')
django.setup()

from core.models import Crop, Advisory, MarketPrice
import random
from decimal import Decimal

def run():
    print("Clearing old data...")
    Crop.objects.all().delete()
    Advisory.objects.all().delete()
    MarketPrice.objects.all().delete()

    print("Populating Crops...")
    wheat = Crop.objects.create(name="Wheat", ideal_season="Winter", ideal_soil_type="Loamy", description="A staple crop worldwide.")
    rice = Crop.objects.create(name="Rice", ideal_season="Monsoon/Summer", ideal_soil_type="Clay", description="Needs high water supply.")
    corn = Crop.objects.create(name="Corn", ideal_season="Summer", ideal_soil_type="Loamy", description="Widely cultivated cereal.")
    
    print("Populating Advisories...")
    Advisory.objects.create(crop=wheat, title="Fertilizer Timing", recommendation="Apply nitrogen fertilizer 3 weeks after sowing.", season="Winter")
    Advisory.objects.create(crop=wheat, title="Weed Control in Loamy soil", recommendation="Use Broad-leaf weedicides after 30 days. Perfect for Loamy soils.", season="Winter")
    Advisory.objects.create(crop=rice, title="Water Management", recommendation="Maintain 2-inches of standing water during the vegetative stage.", season="Monsoon")
    Advisory.objects.create(crop=corn, title="Pest Avoidance", recommendation="Spray neem oil early in the season to prevent stalk borers.", season="Summer")

    print("Populating Market Prices...")
    regions = ["California", "Texas", "Midwest", "Florida", "New York"]
    crops = ["Wheat", "Rice", "Corn", "Soybean", "Tomato"]
    
    for _ in range(15):
        MarketPrice.objects.create(
            crop_name=random.choice(crops),
            region=random.choice(regions),
            price_per_kg=Decimal(random.uniform(5.0, 50.0)).quantize(Decimal('0.00'))
        )

    print("Database successfully populated with mock data!")

if __name__ == '__main__':
    run()
