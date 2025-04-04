from flask import Flask, render_template, request, redirect, url_for # type: ignore
from questions import questions 

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        # Processar respostas
        score = 0
        for i, q in enumerate(questions):
            user_answer = request.form.get(f"q{i}")
            if user_answer == q["answer"]:
                score += 1
        return redirect(url_for("result", score=score, total=len(questions)))
    
    # Exibir o formulário de perguntas
    return render_template("quiz.html", questions=questions)

@app.route("/result")
def result():
    score = int(request.args.get("score"))
    total = int(request.args.get("total"))
    return render_template("result.html", score=score, total=total)

if __name__ == "__main__":
    app.run(debug=True)