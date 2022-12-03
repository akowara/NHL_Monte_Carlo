$( document ).ready(function() {
    $.ajax({url: "/getScores", success: function(result){
      var parsed = JSON.parse(result);
      parsed.forEach((game)=>{
        $("#schedule-body").append("<tr>");
        $("#schedule-body").append("<td>"+game.date+"</td>")
        if(game.score>=0){
          $("#schedule-body").append("<td class = 'winner'>"+game.home+"</td>");
          $("#schedule-body").append("<td>"+game.visitor+"</td>");
        }else if(game.score<0){
          $("#schedule-body").append("<td>"+game.home+"</td>");
          $("#schedule-body").append("<td class = 'winner'>"+game.visitor+"</td>");
        }
        $("#schedule-body").append("<td>"+Math.abs(game.score)+"</td>");
        $("#schedule-body").append("</tr>");
      });
    }});
});
