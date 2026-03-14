import joblib
import pandas as pd

# Load the ML components 
model = joblib.load('dog-classifier')
breed_names = joblib.load('breed_names.joblib')
scaler = joblib.load('scaler.joblib')

def get_dog_recommendations(f, l, s, g, e, c, i, sh, h, w, dt, herd, houn, NS, S, stand, terr, toy, work):
    # 1. Prepare column names to avoid the UserWarning
    feature_names = [
        'Friendly Rating (1-10)', 'Life Span', 'Size', 'Grooming Needs', 
        'Exercise Requirements (hrs/day)', 'Good with Children', 
        'Intelligence Rating (1-10)', 'Shedding Level', 'Health Issues Risk', 
        'Average Weight (kg)', 'Training Difficulty (1-10)', 'Herding', 
        'Hound', 'Non-Sporting', 'Sporting', 'Standard', 'Terrier', 'Toy', 'Working'
    ]

    # 2. Create DataFrame and Scale
    raw_data = pd.DataFrame([[f, l, s, g, e, c, i, sh, h, w, dt, herd, houn, NS, S, stand, terr, toy, work]], 
                            columns=feature_names)
    user_input_scaled = scaler.transform(raw_data)
    
    # 3. Predict
    distances, indices = model.kneighbors(user_input_scaled, n_neighbors=3)
    
    # 4. Return the results as a list instead of printing
    results = []
    for j in range(3):
        idx = indices[0][j]
        results.append(breed_names[idx])
    
    return results