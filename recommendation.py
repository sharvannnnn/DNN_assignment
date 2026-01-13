
def recommend_cosmetics(skin_type):
    recommendations = {
        "Normal Skin": "Maintain balance with gentle cleanser and moisturizer.",
        "Dry Skin": "Use hydrating cleansers and rich moisturizers.",
        "Oily Skin": "Oil-free products with salicylic acid.",
        "Sensitive Skin": "Fragrance-free and hypoallergenic products.",
        "Scaly Skin": "Exfoliation with deep moisturization.",
        "Red_Spots_skin": "Soothing and anti-inflammatory products.",
        "Skin_moles": "Sun protection and dermatologist consultation."
    }
    return recommendations.get(skin_type, "No recommendation available")
