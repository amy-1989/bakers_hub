const deletePostModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deletePostButtons = document.getElementsByClassName("btn-post-delete");
const deletePostConfirm = document.getElementById("deleteConfirm");

/**
* Initializes delete functionality for the provided delete post buttons.
* 
* For each button in the `deletePostButtons` collection:
* - Retrieves the associated post's ID upon click.
* - Updates the `deletePostConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

for (let button of deletePostButtons) {
  button.addEventListener("click", (e) => {
    let postId = e.target.getAttribute("post_id");
    document.getElementById("deleteModalLabel").innerHTML = "Delete Recipe?";
    document.getElementById("modalBodyContent").innerHTML = "Are you sure you want to delete your Recipe? This action cannot be undone." 
    deletePostConfirm.href = `delete_post/${postId}`;
    deletePostModal.show();
  });
}
  