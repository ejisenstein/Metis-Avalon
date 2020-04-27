
          #
          #       <div class="form-group">
          #   {{ sub_team_form.submit(class="btn btn-outline-info")}}
          # </div>
#       <div class="form-group">
#     {{ sub_team_form.submit(class="btn btn-outline-info")}}
# </div>

# if sub_team_form.validate_on_submit:
#     # for r in res:
#     #     if r.team_order != 1:
#     #         r.team_order -=1
#     #     else:
#     #         r.team_order = num_of_players
#         db.session.commit()
#         flash('Count of players shifted')
#sub_team_form=sub_team_form, quest_vote=quest_vote
# <div class="form-group">
#   {{ quest_vote.yes(class="btn btn-outline-info")}}
#   {{ quest_vote.no(class="btn btn-outline-info")}}
# </div>


# res = User.query.order_by(User.team_order).all()
# out = User.query.filter_by(join_game=True).count()

    #order_of_players = User.query.order_by(User.team_order.asc()).all()

# order_of_players = User.query.order_by(User.team_order.asc()).all()


# <ol>
#   {%for r in order_of_players%}
#     <li>{{r}}</li>
#   {%endfor%}
# </ol>
#
#
#   <div class="content-section">
#     <form method="POST" action="">
#         {{ form.hidden_tag() }}
#           <fieldset class = "form-group">
#             <legend class = "border-bottom mb-4">Enter email and click join to begin game</legend>
#
#         </fieldset>
#         <div class="form-group">
#           {{ form.submit(class="btn btn-outline-info")}}
#         </div>
#     </form>
#   </div>
#
#
#   {% elif ((form.validate_on_submit()) and (active_players == num_of_players)) %}
#   <p>Number of users on page is {{ active_players }}</p>

{% for users in joined_players %}
<input type="submit" name="buttons"
  value={{ users.username }}
  style="color:red"
  onclick="color:blue"
>
{% endfor %}
{% for users in joined_players%}
  <input type="checkbox" value="{{users.username}}" name="checker">
  <label{{users.username}}></label>

{%endfor%}
            #
            # {% for users in joined_players %}
            # <input type="submit" name="buttons"
            #   value={{ users.username }}
            #   style="color:red"
            #   onclick="color:blue"
            # >
            # {% endfor %}
