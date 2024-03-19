const editReplyButtons = document.getElementsByClassName("btn-reply-edit");
const replyText = document.getElementById("id_body");
const replyForm = document.getElementById("replyForm");
const submitReplyButton = document.getElementById("replyButton");

const deleteReplyModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteReplyButtons = document.getElementsByClassName("btn-reply-delete");
const deleteReplyConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit reply functionality for the provided edit reply buttons.
* 
* For each button in the `editReplyButtons` collection:
* - Retrieves the associated reply's ID upon click.
* - Fetches the content of the corresponding reply.
* - Populates the `replyText` input/textarea with the reply's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_reply/{replyId}` endpoint.
*/

for (let button of editReplyButtons) {
    button.addEventListener("click", (e) => {
      let replyId = e.target.getAttribute("reply_id");
      let replyContent = document.getElementById(`reply${replyId}`).innerText;
      replyText.value = replyContent;
      submitReplyButton.innerText = "Update";
      replyForm.setAttribute("action", `edit_reply/${replyId}`);
    });
  }

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
  

