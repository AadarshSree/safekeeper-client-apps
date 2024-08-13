async function btnClick() {
    alertify.set("notifier", "position", "top-right");

    let formDetails = {

        username: document.getElementById("usernameField").value,
        password: document.getElementById("passwordField").value,
    };

    // alertify.success(
    //     "Login Form Details: " +

    //     formDetails.username +
    //     " | " +
    //     formDetails.password
    // );

    //
    try {
        let sgx_hmac = await sgxHmacUserPassword(formDetails.password);
        alertify.message("SGX HMAC: " + sgx_hmac);


        // qwertyuiop --hmac--> c503d26078d6f41943cc1b440ccb71c6023fa4b0ae6d9a9c9abc4e9a7962bf5d

        if(sgx_hmac == "c503d26078d6f41943cc1b440ccb71c6023fa4b0ae6d9a9c9abc4e9a7962bf5d" && formDetails.username == "batman"){

            alertify.alert("Login Successful!")
        }
        else{
            if(formDetails.username == "batman")
                alertify.error("Invalid Credentials!")
            else
                alertify.error("User not found, Register first!")
        }
    } catch (error) {
        console.error(error);
    }
}


async function startOnLoad() {
    console.log("[*] LoginPage");

    try {
        await dhkeKeyGen();
        alertify.set("notifier", "position", "top-right");
        alertify.success("Safekeeper Connection Established!");
    } catch (error) {
        console.log("Safekeeper Connection Failed");
        alertify.set("notifier", "position", "top-right");
        alertify.error("Error Establishing Connection to Safekeeper");
        document.getElementById("submitBtn").disabled = true;
        document.getElementById("submitBtn").innerHTML = "DISABLED";
    }

    const submitBtn = document.getElementById('submitBtn');
    submitBtn.onclick = btnClick
}


window.addEventListener('load', startOnLoad);