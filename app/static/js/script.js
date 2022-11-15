/* -------------------
Only frontend script (with no django blocks)
-------------------- */

// 1) Function pulse

(function pulse () {
	$('.txt-pulse').fadeOut(1000).fadeIn(1000, pulse);
})();

// 2) Function to validate newsletter input

function validateEmail(email) {
	const regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
	return regex.test(email);
}

function validateForm() {
	const email = document.getElementById("email").value;
	if (email == "") {
		swal("Opss !", "Você deve digitar o seu email.", "info");
		return false;
	}
	else if (!(validateEmail(email))) {
		document.getElementById('email').value = '';
		swal("Opss !", "Email inválido.", "error");
		return false;
	}
	else { return true; }
}

$(".btn-add").bind("click", validateForm);

// 3) Enable backend button if changes exist
const form = document.querySelectorAll("input");
for (const data of form) {
    data.saved = data.value;
}
// Statement
(btnEnabled = function () {
    var btn = true;
    for (const data of form) {
        if (data.saved !== data.value) {
            btn = false;
            break;
        }
    }
    $("#save-timer, #save-typed, #save-music, #save-home, #save-image").prop("disabled", btn);
})();
// Calling the function
document.oninput = btnEnabled