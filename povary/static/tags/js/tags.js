$(document).ready(function()
    {
        $("input:submit").click(function(e){
            var tag_list = "";
            $("#mytags").find(".tagit-choice").each(function(k, v){
                tag_list += $(v).find('span').text() + ',';
            });
            $("#id_tags").val(tag_list);
        });
        $("#mytags").tagit({
            singleField: true,
            singleFieldNode: $('#id_tags'),
            allowSpaces: true,
            minLength: 2,
            removeConfirmation: true,
            // onTagAdded: function(a, b){
            //     // var tag_title = b.find('span.tagit-label').text();
            //     // var prev_val = $("#id_tags").val();
            //     // $("#id_tags").val(prev_val + ", " + tag_title);
            //     // console.log(b);
            //     var tag_list = "";
            //     $("#mytags").find(".tagit-choice").each(function(k, v){
            //         tag_list += $(v).find('span').text() + ',';
            //     });
            //     $("#id_tags").val(tag_list);

            // },
            tagSource: function( request, response )
                {
                    $.ajax(
                    {
                        url: "/tags/search_tag/", 
                        data: { term:request.term },
                        dataType: "json",
                        success: function( data )
                            {
                                response(
                                    $.map(
                                        data,
                                        function( item )
                                        {
                                            return {
                                                label: item.label+" ("+ item.id +")",
                                                value: item.value
                                            }
                                        }
                                    )
                                );
                            }
                    });
                }
            });
    }
);