document.addEventListener("DOMContentLoaded", function () {
    const articleGenre = document.querySelector(".article-genre");
    const articleList = articleGenre.querySelector(".article-genre-list");
  
    // Bắt sự kiện click trên tiêu đề
    articleGenre.querySelector("h8").addEventListener("click", function () {
      articleGenre.classList.toggle("active");
    });
});