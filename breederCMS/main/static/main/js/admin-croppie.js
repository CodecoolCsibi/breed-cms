$(document).ready(function () {
    var containerElement = document.getElementsByClassName('field-cropped_picture');
    containerElement.tagName = 'croppie-div';
    var croppie = new Croppie(containerElement, {
        viewport: {width: 100, height: 100},
        boundary: {width: 300, height: 300},
        showZoomer: false,
        enableOrientation: true
    });
    var currentImageSource = $('p.file-upload').children('a').src;
    croppie.bind({
        url: currentImageSource
    });
    containerElement.append(
        '<button class="btn btn-primary" id="rotate-left"><i class="fa fa-rotate-left fa-2x"></button>' +
        '<button class="btn btn-primary" id="rotate-right"><i class="fa fa-rotate-right fa-2x"></button>'
    );
    $('#rotate-left').on('click', function () {
        croppie.rotate(-90);
    });
    $('#rotate-right').on('click', function () {
        croppie.rotate(90);
    });
    $('[name="continue"], [name="_addanother"],[name="save"]').on('click', function () {
        croppie.result('blob').then(function (blob) {
            //save BLOB
        })
    })
});
