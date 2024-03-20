const deleteReplyModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteReplyButtons = document.getElementsByClassName("btn-reply-delete");
const deleteReplyConfirm = document.getElementById("deleteConfirm");

  /**
* Initializes delete functionality for the provided delete reply buttons.
* 
* For each button in the `deleteReplyButtons` collection:
* - Retrieves the associated reply's ID upon click.
* - Updates the `deleteReplyConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/

  for (let button of deleteReplyButtons) {
    button.addEventListener("click", (e) => {
      let replyId = e.target.getAttribute("reply_id");
      document.getElementById("deleteModalLabel").innerHTML = "Delete reply?";
      document.getElementById("modalBodyContent").innerHTML = "Are you sure you want to delete your reply? This action cannot be undone." 
      deleteReplyConfirm.href = `delete_reply/${replyId}`;
      deleteModal.show();
    });
  }
  

