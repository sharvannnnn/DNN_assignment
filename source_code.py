import os
from flask import Flask, redirect, render_template, request
from PIL import Image
import torchvision.transforms.functional as TF
import CNN
import numpy as np
import torch
import pandas as pd
import csv

supplement_info =
pd.read_csv(&#39;supplement_info.csv&#39;,encoding=&#39;cp1252&#39;)
model = CNN.CNN(39)
# model.load_state_dict(torch.load(&quot;plant_disease_model_1_latest.pt&quot;))
model.eval()

  def recommend_cosmetics(skin_type):
    if skin_type == &quot;Normal Skin&quot;:
    return &quot;&quot;&quot;For normal skin, you&#39;re lucky to have a well-balanced
complexion.
Your primary goal is to maintain your skin&#39;s health. Here&#39;s a comprehensive
skincare routine:
1. Cleanser: Use a gentle, sulfate-free cleanser to remove impurities.
2. Moisturizer: Opt for a lightweight, non-comedogenic moisturizer.
3. Sunscreen: Apply a broad-spectrum sunscreen daily to protect your skin.
4. Optional: You can incorporate a mild exfoliant 1-2 times a week for extra glow.
&quot;&quot;&quot;
elif skin_type == &quot;Sensitive Skin&quot;:
return &quot;&quot;&quot;Sensitive skin requires extra care to minimize irritation and
redness. Consider
these steps:
1. Cleanser: Use a fragrance-free, hypoallergenic cleanser.
2. Moisturizer: Choose a product with soothing ingredients like aloe vera or chamomile.
3. Sunscreen: Use a physical sunscreen with zinc oxide or titanium dioxide.
4. Avoid harsh exfoliants and strong active ingredients, and patch-test new products.
&quot;&quot;&quot;
elif skin_type == &quot;Dry Skin&quot;:
return &quot;&quot;&quot;Dry skin needs intense hydration and protection. Follow this
regimen:
1. Cleanser: Use a hydrating, gentle cleanser.
2. Moisturizer: Opt for a rich, creamy moisturizer with ingredients like hyaluronic acid
or ceramides.
3. Sunscreen: Apply a broad-spectrum sunscreen daily to prevent further dryness.
4. Consider adding a hydrating serum or facial oil to your routine for added moisture.
&quot;&quot;&quot;
elif skin_type == &quot;Oily Skin&quot;:
return &quot;&quot;&quot;To control excess oil and minimize breakouts, follow these
steps:
1. Cleanser: Use a foaming, salicylic acid-based cleanser to control oil.
2. Moisturizer: Choose an oil-free, lightweight, and non-comedogenic moisturizer.
3. Sunscreen: Use an oil-free, mattifying sunscreen.
4. Consider using products with ingredients like salicylic acid, niacinamide, or witch
hazel to manage oil and acne.
&quot;&quot;&quot;
elif skin_type == &quot;Scaly Skin&quot;:
return &quot;&quot;&quot;Scaly skin often results from dryness and flakiness. Try
these skincare steps:
1. Cleanser: Use a gentle exfoliating cleanser to remove dead skin cells.
2. Moisturizer: Choose a rich, emollient moisturizer to lock in moisture.
3. Sunscreen: Protect your skin from further damage with a daily sunscreen.
4. Exfoliate with products containing glycolic acid or lactic acid to improve texture.
&quot;&quot;&quot;
elif skin_type == &quot;Red_Spots_skin&quot;:
return &quot;&quot;&quot;Red spots can be due to various causes. Here&#39;s a
general approach:
1. Cleanser: Use a gentle, fragrance-free cleanser to avoid irritation.
2. Moisturizer: Select a calming and hydrating moisturizer.
3. Sunscreen: Shield your skin from further damage with a broad-spectrum sunscreen.
4. Consult a dermatologist to identify the specific cause of redness and receive tailored
treatment.
&quot;&quot;&quot;
elif skin_type == &quot;Skin_moles&quot;:
return &quot;&quot;&quot;Moles are usually harmless but require care. Follow these
guidelines:
1. Sunscreen: Protect your skin with a broad-spectrum sunscreen to prevent sun damage.
2. Regularly examine your moles for any changes in size, shape, or color.
3. If you notice changes in a mole, consult a dermatologist for a thorough evaluation.
4. Avoid sun exposure, and consider wearing protective clothing and hats.
&quot;&quot;&quot;
else:
return &quot;Please enter a valid skin type.&quot;
def prediction(image_path):
import tensorflow as tf
model = tf.keras.models.load_model(&#39;skin/skin/model.h5&#39;)
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings(action=&#39;once&#39;)
from tensorflow.keras.preprocessing import image
def prepare(img_path):
img = image.load_img(img_path, target_size=(224,224))
x = image.img_to_array(img)
x = x/255
return np.expand_dims(x, axis=0)
img_path = image_path
predictions = model.predict([prepare(img_path)])
skin_types =[&#39;Red_Spots_skin&#39;, &#39;Dry Skin&#39;, &#39;Normal
Skin&#39;, &#39;Oily Skin&#39;, &#39;Scaly Skin&#39;,
&#39;Sensitive Skin&#39;, &#39;Skin_moles&#39;]
predicted_skin_type = skin_types[np.argmax(predictions)]
# print(f&#39;Predicted Skin Type: {predicted_skin_type}&#39;)
# # Generate skincare recommendations based on the predicted skin type
# recommendations = recommend_cosmetics(predicted_skin_type)
# print(&#39;Skincare Recommendations:&#39;)
# print(recommendations)
return predicted_skin_type
app = Flask(__name__)
@app.route(&#39;/&#39;)

  def home_page():
return render_template(&#39;home.html&#39;)
@app.route(&#39;/contact&#39;)

  def contact():
return render_template(&#39;contact-us.html&#39;)
@app.route(&#39;/index&#39;)

  def ai_engine_page():
return render_template(&#39;index.html&#39;)
@app.route(&#39;/mobile-device&#39;)

  def mobile_device_detected_page():
return render_template(&#39;mobile-device.html&#39;)
@app.route(&#39;/submit222&#39;, methods=[&#39;POST&#39;])

  def submit222():
text = request.form[&#39;textfield&#39;]
with open(&#39;data.csv&#39;, &#39;a&#39;, newline=&#39;&#39;) as csvfile:
fieldnames = [&#39;text&#39;]
writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
writer.writerow({&#39;text&#39;: text})
return &#39;Review submitted successfully!&#39;
@app.route(&#39;/submit&#39;, methods=[&#39;GET&#39;, &#39;POST&#39;])

                def submit():
if request.method == &#39;POST&#39;:
image = request.files[&#39;image&#39;]
filename = image.filename
file_path = os.path.join(&#39;static/uploads&#39;, filename)
image.save(file_path)
print(file_path)
pred = prediction(file_path)
# title = disease_info[&#39;disease_name&#39;][pred]
# description =disease_info[&#39;description&#39;][pred]
# prevent = disease_info[&#39;Possible Steps&#39;][pred]
# image_url = disease_info[&#39;image_url&#39;][pred]
# supplement_name = supplement_info[&#39;supplement name&#39;][pred]
# supplement_image_url = supplement_info[&#39;supplement image&#39;][pred]
# supplement_buy_link = supplement_info[&#39;buy link&#39;][pred]
# return render_template(&#39;submit.html&#39; , title = title , desc = description ,
prevent =prevent ,
#image_url = image_url , pred = pred ,sname = supplement_name ,
simage = supplement_image_url , buy_link = supplement_buy_link)
# # Generate skincare recommendations based on the predicted skin type
recommendations = recommend_cosmetics(pred)
print(&#39;Skincare Recommendations:&#39;)
print(recommendations)
return render_template(&#39;submit.html&#39; , pred =
pred,recommendations=recommendations)
@app.route(&#39;/market&#39;, methods=[&#39;GET&#39;, &#39;POST&#39;])

  def market():
return render_template(&#39;market.html&#39;, supplement_image =
list(supplement_info[&#39;supplement image&#39;]),
supplement_name = list(supplement_info[&#39;supplement
name&#39;]),disease_name= list(supplement_info[&#39;disease_name&#39;]), buy =
list(supplement_info[&#39;buy link&#39;]))

     if __name__ == &#39;__main__&#39;:
app.run(debug=True)
