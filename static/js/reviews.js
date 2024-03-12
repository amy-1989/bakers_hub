const editReviewButtons = document.getElementsByClassName("btn-rating-edit");
const reviewBody = document.getElementById("id_rating");
const ratingForm = document.getElementById("ratingForm");
const submitReviewButton = document.getElementById("submitReviewButton");

const deleteReviewModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteReviewButtons = document.getElementsByClassName("btn-rating-delete");
const deleteReviewConfirm = document.getElementById("deleteConfirm");

for (let button of editReviewButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    let reviewRating = document.getElementById(`review${reviewId}`);
    reviewBody.value = reviewRating;
    submitReviewButton.innerText = "Update";
    ratingForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}

for (let button of deleteReviewButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("review_id");
      document.getElementById("deleteModalLabel").innerHTML = "Delete rating?";
      document.getElementById("modalBodyContent").innerHTML = "Are you sure you want to delete your rating? This action cannot be undone." 
      deleteReviewConfirm.href = `delete_review/${reviewId}`;
      deleteModal.show();
    });
  }
  