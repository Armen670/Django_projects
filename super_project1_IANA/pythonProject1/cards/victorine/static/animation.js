<script>
    let currentIndex = 0;
    const questions = [{ text: "Вопрос 1", translation: "Ответ на вопрос 1" }, { text: "Вопрос 2", translation: "Ответ на вопрос 2" }];

    function showNextPair() {
        if (currentIndex < questions.length) {
            document.getElementById("questionText").innerText = questions[currentIndex].text;
            document.getElementById("answerText").innerText = questions[currentIndex].answer;
            currentIndex++;
        } else {
            alert("Больше вопросов нет.");
        }
    }
</script>