function number_of_checked(checkbox_group) {
    var cnt = 0;
    $('input:checkbox[checkbox_group="' + checkbox_group + '"]').each(function (i, e) {
        if ($(e).prop('checked'))
            ++cnt;
    });
    return cnt;
}

function change_checked(checkbox_group, val) {
    val = !!val;
    $('input:checkbox[checkbox_group="' + checkbox_group + '"]').prop('checked', val);
}