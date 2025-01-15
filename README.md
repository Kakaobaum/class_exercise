### Class Exercise: Building a Streamlit App with the Iris Dataset

#### Objective:
In this exercise, students will deploy a machine learning model using Streamlit to classify iris species. The exercise will guide students to:
1. Load the iris dataset.
2. Collect user input for features.
3. Train and use a `RandomForestClassifier` for predictions.

#### Exercise Duration:
10 minutes.

---

### Step-by-Step Instructions:

1. **Import Necessary Libraries**
   - Start by importing `streamlit`, `pandas`, `numpy`, and `RandomForestClassifier` from `sklearn.ensemble`.

2. **Set Application Title**
   - Add a title and description to the Streamlit app:
     ```python
     st.title('Iris Classification 🌸')
     st.info('Classify Iris species with a Machine Learning model')
     ```

3. **Load and Display the Dataset**
   - Load the Iris dataset from the provided URL:
     ```python
     df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/iris.csv')
     st.write('**Iris Dataset**')
     st.write(df)
     ```

4. **Set Up User Input (Sidebar)**
   - Collect feature values from the user using sliders and dropdowns:
     ```python
     with st.sidebar:
         st.header('Input features')
         sepal_length = st.slider('Sepal Length (cm)', 4.3, 7.9, 5.8)
         sepal_width = st.slider('Sepal Width (cm)', 2.0, 4.4, 3.0)
         petal_length = st.slider('Petal Length (cm)', 1.0, 6.9, 4.35)
         petal_width = st.slider('Petal Width (cm)', 0.1, 2.5, 1.3)

         input_data = {
             'sepal_length': sepal_length,
             'sepal_width': sepal_width,
             'petal_length': petal_length,
             'petal_width': petal_width
         }
         input_df = pd.DataFrame(input_data, index=[0])
     ```

5. **Data Preparation**
   - Separate features (X) and target labels (Y):
     ```python
     X = df.drop('Species', axis=1)
     Y = df['Species']
     ```

   - Encode target labels:
     ```python
     target_mapping = {'setosa': 0, 'versicolor': 1, 'virginica': 2}
     Y_encoded = Y.map(target_mapping)
     ```

6. **Train the RandomForest Model**
   - Initialize and train the model:
     ```python
     clf = RandomForestClassifier()
     clf.fit(X, Y_encoded)
     ```

7. **Make Predictions**
   - Predict species based on user input:
     ```python
     prediction = clf.predict(input_df)
     prediction_proba = clf.predict_proba(input_df)
     ```

8. **Display Results**
   - Show prediction probabilities and the predicted species:
     ```python
     st.write('**Prediction Probabilities**')
     prob_df = pd.DataFrame(prediction_proba, columns=['Setosa', 'Versicolor', 'Virginica'])
     st.write(prob_df)

     st.subheader('Predicted Species')
     species_mapping = {0: 'Setosa', 1: 'Versicolor', 2: 'Virginica'}
     st.success(species_mapping[prediction[0]])
     ```

---

### Deliverables for Students:
- A fully functional Streamlit app that can classify iris species based on user input.

---

### Exercise Goal:
Students learn how to load data, create a machine learning pipeline, collect user inputs, and display predictions using Streamlit in under 10 minutes!
