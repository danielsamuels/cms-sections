$(window).load(function() {
  var $sections = $('div[class*="section_set"]');

  renderSectionFields();

  $sections.find('.field-type select').change(renderSectionFields);

  $(document).on("change", ".dynamic-contentsection_set .field-type select", renderSectionFields);
  // As jQuery event bindings are 'first come first served',
  // showHideSectionFields will be called after the default 'add another
  // section' handler is called. So this will work!
  // (It'll also be fired when *any* 'add another' button is pressed, but)
  // this is harmless.)
  $(".add-row a").click(renderSectionFields);

  function renderSectionFields() {
    var $sections = $('div[class*="section_set"]');

    var types = {
      '': [],
      'homepage-hero': ['title', 'text', 'button_text', 'button_url', 'video', 'logo_set', 'logo_set_title'],
      'landing-hero': ['title', 'text', 'background_image', 'image', 'button_text', 'button_url'],
      'dynamic-demonstration': ['title', 'content', 'button_text'],
      'feature-carousel': ['feature_carousel'],
      'feature-cards': ['title', 'text', 'feature_cards'],
      'benefit-carousel': ['title', 'text', 'benefit_carousel'],
      'cards': ['title', 'text', 'cards', 'background_image', 'background_color'],
      'people': ['title', 'text', 'people'],
      'feature-page-cards': ['title', 'text', 'feature_page_cards', 'background_image'],
      'dual-column': ['background_color', 'title', 'text', 'content_left', 'content_right', 'button_text', 'button_url', 'vertical_alignment'],
      'quote': ['quote', 'quote_logo', 'quote_author', 'quote_author_company', 'background_image', 'logo_set', 'logo_set_title'],
      'quote-with-image': ['quote', 'quote_author', 'quote_author_company', 'background_image'],
      'raw-html': ['title', 'text', 'html', 'background_image'],
      'text-left-image-right': ['content', 'image'],
      'text-right-image-left': ['content', 'image'],
      'content': ['content'],
      'image': ['image'],
      'keyline': [],
      'form': ['form'],
    };

    $sections.each(function () {
      // Define our section
      var $section = $(this);

      // We get the select so we can exclude it from the fields list and we can
      // also check if it has a value to see if hidden fields should be rendered
      var $select = $('.field-type select', $section);

      // These are the fields we will be unhiding
      var fieldsToShow = types[$select.val()];

      // Get all of the fields in the section
      var $fields = $('div[class*="field-"]', $section);

      // Remove the fields we want on every section
      $fields = $fields.not('.field-type, .field-order');

      // Hide all the fields initially
      $fields.hide();

      // If there are fields to show, show them!
      if (fieldsToShow) {
        $.each(fieldsToShow, function (index, field) {
          $section.find('.field-' + field).show();
        });
      }
    });
  }
});
