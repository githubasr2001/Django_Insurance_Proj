from django.shortcuts import render, redirect
import joblib
import numpy as np

def home(request):
    return render(request, "home.html")

def result(request):
    if request.method == 'POST':
        rf = joblib.load('random_forest_regressor.sav')  # Adjust the path as needed

        # Extract and convert form data
        age = int(request.POST.get('age', 0))
        sex = request.POST.get('sex', 'male')
        bmi = float(request.POST.get('bmi', 0))
        children = int(request.POST.get('children', 0))
        smoker = request.POST.get('smoker', 'no')
        region = request.POST.get('region', 'southwest')

        # Convert categorical data to numerical values as expected by the model
        sex = 0 if sex == 'male' else 1
        smoker = 0 if smoker == 'no' else 1

        # Assuming the model was trained with 'region' as a single categorical feature
        # that was numerically encoded (not one-hot encoded).
        # Here, you should convert 'region' into a numerical value based on your model's training.
        # If the model was indeed trained with one-hot encoding for 'region', you need to adjust
        # the number of features your model expects or ensure that 'region' encoding matches the model training.

        # Example: Numerical encoding for 'region' (assuming your model was trained this way)
        # Adjust these values based on your actual model training.
        regions = {'northeast': 0, 'northwest': 1, 'southeast': 2, 'southwest': 3}
        region_num = regions.get(region, 0)  # Default to 0 (northeast) if not found

        # Prepare the input array with the correct number of features
        lis = np.array([age, sex, bmi, children, smoker, region_num]).reshape(1, -1)

        # Predict
        ans = rf.predict(lis)[0]

        return render(request, "result.html", {'ans': ans})
    else:
        # Redirect to home if not a POST request
        return redirect('home')
