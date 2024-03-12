const editReviewButtons = document.getElementsByClassName("btn-rating-edit");
const reviewBody = document.getElementById("id_rating");
const ratingForm = document.getElementById("ratingForm");
const submitReviewButton = document.getElementById("submitReviewButton");

for (let button of editReviewButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    console.log(reviewId);
    let reviewRating = document.getElementById(`review${reviewId}`);
    reviewBody.value = reviewRating;
    submitReviewButton.innerText = "Update";
    ratingForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}