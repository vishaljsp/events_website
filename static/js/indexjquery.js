$(document).click('#lbn',()=>{$(document).on("submit", '#singhupform', (e) => {
    e.preventDefault();
    let numberphone = $('#phoneNumber').val()
    let x = $("#phoneNumber").val()
    let msbtn=$("#lbn")
    if (x.length ==13) {
        otpinput.style.display = "block"
        msbtn.remove()
        // msbtn.style.display = "none"
        $.ajax({
            type: "post",
            url: "/",
            data: {
                num: numberphone,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val()
            },
        })
    }
    else {
        
        let erorhend = $("#errorshowofnumber")
        erorhend.text("Check your number")
    }


})})



