let on_time = 0;
const max_time = 12;
let playing = false;

let notes = []

$(document).ready(function(){
    for(let i = 0; i < max_time; i++){
        notes.push([]);
    }

    $(".note").click(function(){
        if($(this).attr("play") === "0"){
            $(this).attr("play",1);
            $(this).children('i').removeClass("far").addClass("fas");

            notes[$(this).attr("time") - 1] += $(this).attr("note");
        } else{
            $(this).attr("play",0);
            $(this).children('i').removeClass("fas").addClass("far");

            notes[$(this).attr("time") - 1] = notes[$(this).attr("time") - 1].replace($(this).attr("note"), "");
        }
    });

    $(".play-button").click(function(){
        if($(this).attr("play") === "0"){
            $(this).attr("play",1);
            $(this).html('<i class="fas fa-pause"></i>');

            playing=true;
            Play();
        } else {
            $(this).attr('play',0);
            $(this).html('<i class="fas fa-play"></i>');

            playing=false;
        }
    });
});

function Play(){
    if (playing){
        $(".time-" + on_time).each(function(index){
            $(this).removeClass("current");
        });

        if (on_time===max_time){
            on_time = 0;
        }
        on_time += 1;

        $(".time-" + on_time).each(function(index){
            $(this).addClass("current");

            if($(this).attr("play") === "1"){
                $("#" + $(this).attr("note") + "-" + $(this).attr("time"))[0].load();
                $("#" + $(this).attr("note") + "-" + $(this).attr("time"))[0].play();
            }
        });

        setTimeout( function(){
            Play();
        },500);
    }
}
