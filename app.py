from flask import Flask, render_template, request, redirect, url_for
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
    import os
    port = int(os.environ.get("PORT", 5000))  # Usa a porta fornecida pelo Render ou 5000 como padrão
    app.run(host="0.0.0.0", port=port)       # Escuta em 0.0.0.0