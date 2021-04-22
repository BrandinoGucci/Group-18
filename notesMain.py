












@app.route('/')
@app.route('/home')
def home()




@app.route('/events')
def events()





@app.route('/events/<note_id>')
def events(note_id)




@app.route('/events/new', methods=['GET', 'POST'])
def new_event()



@app.route('/events/edit/<note_id>', methods=['GET', 'POST'])
def update_event()


@app.route('/events/rsvp')
def rsvp_event()


@app.route('/events/delete/<note_id>', methods=['POST'])
def delete_event(note_id):



@app.route('/register', methods=['POST', 'GET'])
def register():



@app.route('/login', methods=['POST', 'GET'])
def login():




@app.route('/logout')
def logout():

