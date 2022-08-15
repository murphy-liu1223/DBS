{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, request\n",
    "import joblib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "method = ['GET','POST']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "@app.route('/', methods = ['GET','POST'])\n",
    "def index():\n",
    "    if request.method == 'POST':\n",
    "        rates = float(request.form.get('rates'))\n",
    "        model_reg = joblib.load('regression_DBS')\n",
    "        result_reg = model_reg.predict([[rates]])\n",
    "        model_tree = joblib.load('tree_DBS')\n",
    "        result_tree = model_tree.predict([[rates]])\n",
    "        return(render_template('index.html', result1 = result_reg, result2 = result_tree))\n",
    "    else:\n",
    "        return(render_template('index.html', result1 = 'waiting', result2 = 'waiting'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://localhost:5001/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run(host='localhost', port=5001, debug=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
