document.addEventListener('DOMContentLoaded', () => {
    // Текущий пользователь и статья
    const currentUser = "user1"; // Имитируем текущего пользователя
    const article = {
        id: 1,
        title: "Моя статья",
        content: "Это пример текста статьи.",
        author: "user1", // Автор статьи
    };

    const titleInput = document.getElementById("article-title");
    const contentInput = document.getElementById("article-content");
    const errorMessage = document.getElementById("error-message");

    // Предзаполнение формы
    titleInput.value = article.title;
    contentInput.value = article.content;

    // Проверка прав редактирования
    if (article.author !== currentUser) {
        document.getElementById("editArticleForm").style.display = "none";
        errorMessage.textContent = "У вас нет прав на редактирование этой статьи.";
        return;
    }

    // Обработка отправки формы
    document.getElementById("editArticleForm").addEventListener("submit", (event) => {
        event.preventDefault();

        const updatedArticle = {
            title: titleInput.value.trim(),
            content: contentInput.value.trim(),
        };

        if (!updatedArticle.title || !updatedArticle.content) {
            errorMessage.textContent = "Пожалуйста, заполните все поля.";
            return;
        }

        console.log("Обновленная статья:", updatedArticle);

        // Эмуляция сохранения
        setTimeout(() => {
            alert("Статья успешно обновлена!");
            window.location.href = `/articles/${article.id}`;
        }, 1000);
    });
});
