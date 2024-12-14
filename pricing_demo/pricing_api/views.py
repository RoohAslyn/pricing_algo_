from django.http import JsonResponse

def adjust_prices(request):
    # Dummy data
    menu = {"Butter Chicken": 12.99, "Naan": 2.99, "Chicken Biryani": 11.99}
    competitors = [{"Butter Chicken": 11.49}, {"Naan": 2.49}, {"Chicken Biryani": 10.99}]
    weather = {"temperature": 44, "condition": "Rain"}
    busy = True

    # Price adjustment logic
    adjusted_menu = {}
    for item, price in menu.items():
        lowest_competitor_price = min(comp.get(item, price) for comp in competitors)
        if weather['temperature'] < 45 or weather['condition'] in ["Rain", "Snow"] or busy:
            adjusted_price = round(lowest_competitor_price * 1.2, 2)  # Increase 20%
        else:
            adjusted_price = lowest_competitor_price
        adjusted_menu[item] = adjusted_price

    return JsonResponse({"menu": adjusted_menu, "weather": weather, "busy": busy})
