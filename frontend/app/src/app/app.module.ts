import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { ParentExampleComponent } from './parent-example/parent-example.component';
import { ChildExampleComponent } from './child-example/child-example.component';
import { ConfigService } from './services/config.service';
import { ContextService } from './services/context.service';
import { ApiService } from './services/api.service';
import { HttpClient } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    ParentExampleComponent,
    ChildExampleComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [
    ConfigService,
    ContextService,
    ApiService,
    HttpClient,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
