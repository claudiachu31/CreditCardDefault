#!/usr/bin/env python
# coding: utf-8

# In[5]:


from flask import Flask


# In[6]:


app = Flask(__name__)


# In[7]:


from flask import request, render_template
import joblib

@app.route("/", methods = ["GET", "POST"])
def index(): 
    model_1 = 'Logistic Regression Model predicts: '
    model_2 = 'Decision Tree Model predicts: '
    model_3 = 'Neural Network Model predicts: '
    model_4 = 'Random Forest Model predicts: '
    model_5 = 'Gradient Booster Model predicts: '
    if request.method == "POST":
        income = request.form.get("income")
        age = request.form.get("age")
        loan = request.form.get("loan")

      
        model = joblib.load("CreditCardREG")
        pred = model.predict([[float(income),float(age),float(loan)]])
        if str(pred)=='[1]': # this is default
            s1 = model_1 + 'Default'
        else:
            s1 = model_1 + 'No Default'
#         s1 = "The credit card default based on Logistic Regression is : " + str(pred)
        
        model = joblib.load("CreditCardDT")
        pred = model.predict([[float(income),float(age),float(loan)]])
        if str(pred)=='[1]': # this is default
            s2 = model_2 + 'Default'
        else:
            s2 = model_2 + 'No Default'
#         s2 = "The credit card default based on Decision Tree model is : " + str(pred)
        
        
        model = joblib.load("CreditCardNN")
        pred = model.predict([[float(income),float(age),float(loan)]])
        if str(pred)=='[1]': # this is default
            s3 = model_3 + 'Default'
        else:
            s3 = model_3 + 'No Default'
#         s3 = "The credit card default based on Neural Network model is : " + str(pred)
        
         
        model = joblib.load("CreditCardRF")
        pred = model.predict([[float(income),float(age),float(loan)]])
        if str(pred)=='[1]': # this is default
            s4 = model_4 + 'Default'
        else:
            s4 = model_4 + 'No Default'
#         s4 = "The credit card default based on Random Forest model is : " + str(pred)
        
         
        model = joblib.load("CreditCardGB")
        pred = model.predict([[float(income),float(age),float(loan)]])
        if str(pred)=='[1]': # this is default
            s5 = model_5 + 'Default'
        else:
            s5 = model_5 + 'No Default'
#         s5 = "The credit card default based on Gradient Booster model is : " + str(pred)
        
        return(render_template("index.html", result1=s1, result2=s2, result3=s3, result4=s4, result5=s5))
    else: 
        s1 = model_1 + 'NA'
        s2 = model_2 + 'NA'
        s3 = model_3 + 'NA'
        s4 = model_4 + 'NA'
        s5 = model_5 + 'NA'
        return(render_template("index.html", result1=s1, result2=s2, result3=s3, result4=s4, result5=s5))
#         return(render_template("index.html", result1="2", result2="2", result3="2", result4="2", result5="2"))
        


# In[ ]:


if __name__=="__main__":
    
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




