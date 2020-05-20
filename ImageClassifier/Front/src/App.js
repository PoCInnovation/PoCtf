
import axios from 'axios';

import React,{Component} from 'react';

class App extends Component {

    state = {

        // Initially, no file is selected
        selectedFile: null,
        flag: ""
    };

    // On file select (from the pop up)
    onFileChange = event => {

        // Update the state
        this.setState({ selectedFile: event.target.files[0] });

    };

    // On file upload (click the upload button)
    onFileUpload = () => {

        if (this.state.selectedFile === null)
            return
        // Create an object of formData
        const formData = new FormData();

        // Update the formData object
        formData.append(
            "myFile",
            this.state.selectedFile,
            this.state.selectedFile.name
        );

        // Details of the uploaded file
        console.log(this.state.selectedFile);

        // Request made to the backend api
        // Send formData object
        axios.post("http://127.0.0.1:5000/api/uploadfile", formData).then((response) => {
            this.setState({flag : response.data});
          }, (error) => {
            console.log(error);
          });
    };

    flagData = () => {
        if (this.state.flag.flag) {
            return <div>
                <h2>Flag: {this.state.flag["flag"]}</h2>
            </div>
        } else if (this.state.flag.NOPE) {
            return <div>
            <h2>NOPE: {this.state.flag["NOPE"]}</h2>
        </div>
        } else {
            return
        }
    }
    // File content to be displayed after
    // file upload is complete
    fileData = () => {
        if (this.state.selectedFile) {

            return (
                <div>
                    <h2>File Details:</h2>
                    <p>File Name: {this.state.selectedFile.name}</p>
                    <p>File Type: {this.state.selectedFile.type}</p>
                </div>
            );
        } else {
            return (
                <div>
                    <br />
                    <h4>Choose before Pressing the Upload button</h4>
                </div>
            );
        }
    };

    render() {

        return (
            <div>
                <h1>
                    PoCTF IA Challenge
                </h1>
                <h3>
                    Upload the image of my dog, and make him a cat.<br/>
                    If it's not my dog i'll know it ! (I've got the best<br/>
                    image verification my dev could do ! It can say if you<br/>
                    changed more than 15 pixels on a pictures ! AHAHAHAHAHAHA !)<br/>
                </h3>
                <div>
                    <input type="file" onChange={this.onFileChange} />
                    <button onClick={this.onFileUpload}>
                        Upload!
                    </button>
                </div>
                {this.fileData()}
                {this.flagData()}
            </div>
        );
    }
}
export default App;

