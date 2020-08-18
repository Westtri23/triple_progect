CKEDITOR.plugins.add( 'abbr', {
    icons: 'icons/abbr.png',
    init: function( editor ) {
        editor.addCommand( 'abbr', new CKEDITOR.dialogCommand( 'abbrDialog' ) );
        editor.ui.addButton( 'Abbr', {
            label: 'Я тут',
            command: 'abbr',
            toolbar: 'insert, 100'
        });

        CKEDITOR.dialog.add( 'abbrDialog', this.path + 'dialogs/abbr.js' );
    }
});