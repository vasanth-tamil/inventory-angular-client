import { Component } from '@angular/core';
import { FormControl, FormGroup, FormsModule, NgForm, ReactiveFormsModule, Validators } from '@angular/forms';
import { User } from '../../../types/user.type';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { ApiConstant } from '../../../constants/api-contants';

@Component({
  selector: 'app-sign-up',
  standalone: true,
  imports: [FormsModule, CommonModule, ReactiveFormsModule],
  templateUrl: './sign-up.component.html',
  styleUrl: './sign-up.component.css'
})
export class SignUpComponent {
  
  signUpForm = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.email]),
    password: new FormControl('', [Validators.required]),
    re_password: new FormControl('', [Validators.required]),
  });

  constructor(private http: HttpClient) { }

  onSignUp() {
    this.signUpForm.markAllAsTouched();
    if(this.signUpForm.valid) {
      this.http.post(ApiConstant.signUp, this.signUpForm.value).subscribe((data) => {
        console.log(data);
        this.signUpForm.reset();
      });
    }
  }

}
