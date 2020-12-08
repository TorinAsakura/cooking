tinyMCE.init({
  // General options
    mode : "textareas",
    theme : "advanced",
    plugins : "spellchecker",
    editor_deselector : "mceNoEditor",
	theme_advanced_buttons1 : "bold,italic,underline,link,unlink,bullist,blockquote,undo", 
    theme_advanced_buttons2 : "spellchecker", 
    theme_advanced_buttons3 : "",
    language : "ru",

  // Spellchecker
    spellchecker_languages : "+Russian=ru,Ukrainian=uk,English=en",
    spellchecker_rpc_url : "http://speller.yandex.net/services/tinyspell",
    spellchecker_word_separator_chars : '\\s!"#$%&()*+,./:;<=>?@[\]^_{|}\xa7\xa9\xab\xae\xb1\xb6\xb7\xb8\xbb\xbc\xbd\xbe\u00bf\xd7\xf7\xa4\u201d\u201c',
});
