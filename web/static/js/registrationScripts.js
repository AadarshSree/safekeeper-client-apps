async function btnClick() {
    alertify.set("notifier", "position", "top-right");

    let formDetails = {
        name: document.getElementById("nameField").value,
        username: document.getElementById("usernameField").value,
        email: document.getElementById("emailField").value,
        password: document.getElementById("passwordField").value,
    };

    alertify.success(
        "Form Details: " +
        formDetails.name +
        " | " +
        formDetails.username +
        " | " +
        formDetails.email +
        " = " +
        formDetails.password
    );

    //
    try {
        let sgx_hmac = await sgxHmacUserPassword(formDetails.password);
        alertify.success("SGX HMAC: " + sgx_hmac);
    } catch (error) {
        console.error(error);
    }
}

async function startOnLoad() {
    console.log("[*] Hello World");

    try {
        await dhkeKeyGen();
        alertify.set("notifier", "position", "top-right");
        alertify.success("Safekeeper Connection Established!");
    } catch (error) {

        if(error.code === "QUOTE_VERIFICATION_FAILED"){

            console.log("SGX Quote Verification Failed");
            alertify.set("notifier", "position", "top-right");
            alertify.error("SGX Quote Verification Failed");
            document.getElementById("submitBtn").disabled = true;
            document.getElementById("submitBtn").innerHTML = "DISABLED";

        }
        else{

            console.log("Safekeeper Connection Failed");
            alertify.set("notifier", "position", "top-right");
            alertify.error("Error Establishing Connection to Safekeeper");
            document.getElementById("submitBtn").disabled = true;
            document.getElementById("submitBtn").innerHTML = "DISABLED";

        }
        
    }

    const submitBtn = document.getElementById('submitBtn');
    submitBtn.onclick = btnClick
}


window.addEventListener('load', startOnLoad);


