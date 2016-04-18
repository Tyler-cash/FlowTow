% rebase('base.tpl')


<h1>Welcome to FlowTow</h1>

<div class='container'>
    <div class="row">
        % import interface
        % import database
        %
        % db = database.COMP249Db()
        %
        % db.create_tables()
        % db.sample_data()
        % images = interface.list_images(db, 1)
        % for image in images:
        % user = image['user']
        % likes = image['likes']
        % timestamp = image['timestamp']
        % filename = image['filename']
        <div class='image col s10 m3 offset-s1 flowtow'>
            <div class="card">
                <div class="card-image waves-effect waves-block waves-light">
                    <img src="/static/images/{{filename}}" alt="window">
                </div>
                <div class="card-content">
                    <p class='user'>{{user}}</p>
                    <p class='likes'>{{likes}} Likes</p>
                    <p class='date'>Uploaded : {{timestamp}}</p>
                </div>
                <div class="card-action">
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


