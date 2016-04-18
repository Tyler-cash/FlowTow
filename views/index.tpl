% rebase('base.tpl')


<h1 class="center" id="welcome-message"><strong>Welcome to FlowTow</strong></h1>

<div class='container'>
    <div class="row">
        % import interface
        % import database
        %
        % db = database.COMP249Db()
        %
        % db.create_tables()
        % db.sample_data()
        % images = interface.list_images(db, 20)
        % for image in images:
        % user = image['user']
        % likes = image['likes']
        % timestamp = image['timestamp']
        % filename = image['filename']
        <div class='image col s10 m3 offset-s1 flowtow'>
            <div class="card">
                <div class="card-image waves-effect waves-block waves-light">
                    <img draggable="false" src="/static/images/{{filename}}" alt="{{filename}}">
                </div>
                <div class="card-content">
                    <p class='user'>{{user}}</p>
                    <p class='likes'>{{likes}} Likes</p>
                    <p class='date'>Uploaded : {{timestamp}}</p>
                </div>
                <div class="card-action  center">
                    <form action="/like">
                        <input type="submit" value="Like" action="/like"><a class="waves-effect waves-light btn">Like</a></input>
                        <input type="submit" action="/like" value="Like" class="hidden">
                    </form>
                </div>
            </div>
        </div>
        %end

    </div>
</div>


