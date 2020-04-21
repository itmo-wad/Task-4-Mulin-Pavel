



new_user = """"INSERT INTO users ( tgID , nickName )
VALUES ( (%tgID) , '(%nickName)' )"""
db_cursor.execute(new_user, [tgID, nickName])
