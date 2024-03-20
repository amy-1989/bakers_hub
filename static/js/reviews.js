const editReviewButtons = document.getElementsByClassName("btn-rating-edit");
const reviewBody = document.getElementById("id_rating");
const ratingForm = document.getElementById("ratingForm");
const submitReviewButton = document.getElementById("submitReviewButton");

const deleteReviewModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteReviewButtons = document.getElementsByClassName("btn-rating-delete");
const deleteReviewConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit review functionality for the provided edit reviews buttons.
* 
* For each button in the `editReviews` collection:
* - Retrieves the associated review's ID upon click.
* - Fetches the content of the corresponding comment.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_review/{reviewId}` endpoint.
*/

for (let button of editReviewButtons) {
  button.addEventListener("click", (e) => {
    let reviewId = e.target.getAttribute("review_id");
    let reviewRating = document.getElementById(`review${reviewId}`);
    reviewBody.value = reviewRating;
    submitReviewButton.innerText = "Update";
    ratingForm.setAttribute("action", `edit_review/${reviewId}`);
  });
}

/**
* Initializes delete functionality for the provided delete review buttons.
* 
* For each button in the `deleteReviewButtons` collection:
* - Retrieves the associated review's ID upon click.
* - Updates the `deleteReviewConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

for (let button of deleteReviewButtons) {
    button.addEventListener("click", (e) => {
      let reviewId = e.target.getAttribute("review_id");
      document.getElementById("deleteModalLabel").innerHTML = "Delete rating?";
      document.getElementById("modalBodyContent").innerHTML = "Are you sure you want to delete your rating? This action cannot be undone." 
      deleteReviewConfirm.href = `delete_review/${reviewId}`;
      deleteReviewModal.show();
    });
  }
