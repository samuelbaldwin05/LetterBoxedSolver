from flask import Flask, render_template, request
from Letterbox_solver import one_two_word_solutions, three_word_solutions 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    three_word_search = False  # Track if three-word solutions are being displayed

    if request.method == 'POST':
        # Get side inputs
        sides = (request.form.get('side1'), request.form.get('side2'), request.form.get('side3'), request.form.get('side4'))
        
        # Check which solution type to use
        if request.form.get('solution_type') == 'three_word':
            # Call the three-word solutions function
            result = three_word_solutions(sides)
            three_word_search = True
        else:
            # Call the one/two-word solutions function by default
            result = one_two_word_solutions(sides)
        
    
    return render_template('letterbox.html', result=result, three_word_search=three_word_search)

if __name__ == '__main__':
    app.run(debug=True)
