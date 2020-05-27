window.onload = function () {
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $('.col').on('click', 'button[id="add"]', function () {
        var href_data = event.target;
        var id = href_data.name

        $.ajax({
            type: "POST",
            url: "/tournaments/" + id + "/add-user/",

            success: function (data) {
                if (data.result) {
                    var alertDelete = '<div class="col"><div class="alert alert-primary"  role="alert">\n'
             + data.result +
            '    <button type="button" class="close" data-dismiss="alert" aria-label="Close">\n' +
            '  <span aria-hidden="true">&times;</span>\n' +
            '</button>\n' +
            '</div></div>'
                    $('div[data-id="' + id + '"]').html(alertDelete);
                    $('button[id="delete"]').css("display", "block")
                    $('button[id="add"]').css("display", "none")
                }
            },
        });

        event.preventDefault();
    });
    $('.col').on('click', 'button[id="delete"]', function () {
        var href_data = event.target;
        var id = href_data.name


        $.ajax({
            type: "POST",
            url: "/tournaments/" + id + "/del-user/",

            success: function (data) {
                if (data.result) {
                    var alertDelete = '<div class="col"><div class="alert alert-primary"  role="alert">\n'
             + data.result +
            '    <button type="button" class="close" data-dismiss="alert" aria-label="Close">\n' +
            '  <span aria-hidden="true">&times;</span>\n' +
            '</button>\n' +
            '</div></div>'
                    $('div[data-id="' + id + '"]').html(alertDelete);
                    $('button[id="delete"]').hide().css("display", "none")
                    $('button[id="add"]').css("display", "block")
                }
            },
        });

        // event.preventDefault();
    });


}