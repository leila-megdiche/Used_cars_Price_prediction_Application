{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "79c60666-065d-42f4-8ca8-77fa69e19d8d",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "#! pip install flask"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "5c8231fb-a1a3-49b6-9567-6b6843b5ab35",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "0f0a7098-5c32-4b92-8920-4b95dcdddc87",
   "metadata": {
    "tags": []
   },
   "outputs": [],
   "source": [
    "model = joblib.load('LassoReg_Model.pkl')\n",
    "preprocessor = joblib.load('preprocessor.pkl')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "8a1c0d3b-b161-4c62-835b-fbd8a6919fbe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      " * Restarting with watchdog (windowsapi)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[1;31mSystemExit\u001b[0m\u001b[1;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\megdiche leila\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\IPython\\core\\interactiveshell.py:3468: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "app = Flask(__name__)\n",
    "\n",
    "@app.route('/', methods=['GET', 'POST'])\n",
    "def index():\n",
    "    if request.method == 'POST':\n",
    "        # Retrieve the input values from the form\n",
    "        car_features = []\n",
    "        car_features.append(request.form['age'])\n",
    "        car_features.append(request.form['CompanyName'])\n",
    "        car_features.append(request.form['km_driven'])\n",
    "        car_features.append(request.form['fuel'])\n",
    "        car_features.append(request.form['seller_type'])\n",
    "        car_features.append(request.form['transmission'])\n",
    "        car_features.append(request.form['owner'])\n",
    "        car_features.append(request.form['mileage'])\n",
    "        car_features.append(request.form['engine'])\n",
    "        car_features.append(request.form['max_power'])\n",
    "        car_features.append(request.form['torque'])\n",
    "        car_features.append(request.form['seats'])\n",
    "        car_features.append(request.form['feature2'])\n",
    "\n",
    "        # Preprocess the input data\n",
    "        transformed_features = preprocessor.transform([car_features])\n",
    "\n",
    "        # Make predictions\n",
    "        predicted_price = model.predict(transformed_features)[0]\n",
    "\n",
    "        # Render the HTML page with the predicted price\n",
    "        return render_template('index.html', predicted_price=predicted_price)\n",
    "\n",
    "    # Render the initial HTML page with the form\n",
    "    return render_template('index.html')\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5dc281fd-15dd-41ac-bf1a-55bafba01229",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
