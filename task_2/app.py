from flask import Flask, request, render_template

app = Flask(__name__)

equations = open('equations.txt').readlines()
answers = [104, 116, 116, 112, 115, 58, 47, 47, 119, 119, 119, 46, 121, 111, 117, 116, 117, 98, 101, 46, 99, 111, 109,
           47, 119, 97, 116, 99, 104, 63, 118, 61, 100, 81, 119, 52, 119, 57, 87, 103, 88, 99, 81, 38, 97, 98, 95, 99,
           104, 97, 110, 110, 101, 108, 61, 82, 105, 99, 107, 65, 115, 116, 108, 101, 121, 38, 38, 102, 108, 97, 103,
           123, 72, 87, 95, 73, 83, 95, 68, 79, 78, 69, 95, 65, 88, 65, 88, 65, 88, 65, 88, 65, 88, 65, 88, 65, 88, 65,
           88, 65, 88, 65, 41, 125]

c = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    global c

    if request.method == 'POST':
        user_answer = int(request.form['user_answer'])
        equation_index = int(request.form['equation_index'])
        correct_answer = answers[equation_index]

        if user_answer == correct_answer:
            c += 1
        else:
            return f"Неправильно. Попробуйте еще раз. <a href='/'>Вернуться</a>"

    equation_index = c
    if c >= len(equations):
        return "Вы решили все уравнения! Теперь сдайте их учителю. Его зовут <a href='/VV1NN3R'>Lion</a>"
    return render_template('index.html', equation_index=equation_index, equation_text=equations[c])


@app.route('/VV1NN3R', methods=['GET'])
def win():
    return render_template('win.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6969)
