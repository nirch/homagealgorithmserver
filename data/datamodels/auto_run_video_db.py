from logic.models.auto_run_video import AutoRunVideo

__author__ = 'danga_000'


from data import db

def get_AutoRunVideo_by_cycleidvideoid(cycleid,videoid):
    query = "SELECT * FROM AutoRunVideo " \
            "WHERE cycle_id = {0} AND video_id = {1}".format(cycleid,videoid)
    cursor = db.get_cursor_from_query(query)
    row = cursor.fetchone()
    autorunvideo = AutoRunVideo(row[0],row[1],row[2],row[3])
    return autorunvideo


def insert_autorunvideo(autorunvideo):
    # Prepare SQL query to INSERT a record into the database.
    query = """INSERT INTO AutoRunVideo(cycle_id,
         video_id, average_score, exception)
         VALUES ({0}, {1}, {2}, {3})""".format(autorunvideo.cycleid,
                                                 autorunvideo.videoid,
                                                 autorunvideo.average_score,
                                                 autorunvideo.exception)
    db.dml(query)

def update_score(autorunvideo,averagescore,exception):
    # Prepare SQL query to UPDATE required records
    query = "UPDATE AutoRunVideo SET average_score = {0}, exception = {1} " \
            "WHERE cycle_id = {2} AND video_id = {3}".format(averagescore,
                                                             exception,
                                                             autorunvideo.videoid,
                                                             autorunvideo.frameid)
    db.dml(query)

def delete_autorunvideo_by_cycleidvideoid(autorunvideo):
    # Prepare SQL query to UPDATE required records
    query = "DELETE FROM AutoRunVideo WHERE cycle_id = {0} AND video_id = {1}".format(autorunvideo.cycleid,autorunvideo.videoid,)
    db.dml(query)