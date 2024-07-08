import { Component } from '@angular/core';
import { FormControl, FormGroup, FormsModule, ReactiveFormsModule, Validators } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { ApiConstant } from '../../../constants/api-contants';
import { SignInResponse } from '../../../types/sign-in-response.type';
import { Router } from '@angular/router';

@Component({
  selector: 'app-sign-in',
  standalone: true,
  imports: [FormsModule, CommonModule, ReactiveFormsModule],
  templateUrl: './sign-in.component.html',
  styleUrl: './sign-in.component.css'
})
export class SignInComponent {

  signInForm = new FormGroup({
    email: new FormControl('', [Validators.required, Validators.email]),
    password: new FormControl('', [Validators.required]),
  });

  constructor(private http: HttpClient, private router: Router) { }

  onSignIn() {
    this.signInForm.markAllAsTouched();
    
    if(this.signInForm.valid) {
      this.http.post<SignInResponse>(ApiConstant.signIn, this.signInForm.value).subscribe((data) => {
        // save token
        localStorage.setItem('token', data.token);
        this.signInForm.reset();
        this.router.navigate(['inventory']);
      });
    }
  }

}
