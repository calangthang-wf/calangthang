document.addEventListener("DOMContentLoaded", function () {
  const articleGenre = document.querySelector(".article-genre");
  const articleList = articleGenre.querySelector(".article-genre-list");

  articleList.style.display = "block";
  
  articleGenre.querySelector("h8").addEventListener("click", function () {
    // Toggle hiển thị/gấp lại danh sách
    if (articleList.style.display === "block") {
      articleList.style.display = "none";
    } else {
      articleList.style.display = "block";
    }
  });
});

document.addEventListener("DOMContentLoaded", function() {
  const contentElements = document.querySelectorAll(".latest-content-items-subcontent");
  const maxLength = 50;

  contentElements.forEach(function(element) {
      const content = element.textContent.trim();
      if (content.length > maxLength) {
          element.textContent = content.substring(0, maxLength) + "...";
      }
  });
});
document.addEventListener("DOMContentLoaded", function() {
  const contentElements = document.querySelectorAll(".popular-posts-subcontent");
  const maxLength = 50;

  contentElements.forEach(function(element) {
      const content = element.textContent.trim();
      if (content.length > maxLength) {
          element.textContent = content.substring(0, maxLength) + "...";
      }
  });
});
document.addEventListener("DOMContentLoaded", function() {
  const contentElements = document.querySelectorAll(".popular-service-items-info");
  const maxLength = 100;

  contentElements.forEach(function(element) {
      const content = element.textContent.trim();
      if (content.length > maxLength) {
          element.textContent = content.substring(0, maxLength) + "...";
      }
  });
});

var items = document.querySelectorAll(".popular-community-items-col");
for (var i = 0; i < items.length; i++) {
    if (i !== items.length - 1) {
        items[i].style.borderBottom = "none";
    }
}
