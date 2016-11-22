__kernel void euler_qinit(__global float* d_q, 
                            const int meqn, const int mx, const int mbc, 
                            const float xlower, const float dx, 
                            const float gamma){
    int i = get_global_id(0);
    float xcell = xlower + dx*(i - mbc + 1 - 0.5);
    /*
    float rho_l = 1.0, rho_r = 1.0/8.0;
    float p_l = 1.0, p_r = 0.1;
    float pressure, velocity;
    
    if(xcell < 0.0){
        d_q[meqn*i] = rho_l;
        pressure = p_l;
    }else{
        d_q[meqn*i] = rho_r;
        pressure = p_r;
    }
    d_q[meqn*i+1] = 0.0;
    velocity = d_q[meqn*i+1]/d_q[meqn*i];
    d_q[meqn*i+2] = pressure/(gamma - 1.0) + 0.5*d_q[meqn*i]*pow(velocity,2);*/
    d_q[meqn*i] = 1.0;
    d_q[meqn*i+1] = 0.0;
    if(xcell < 0.1){
        d_q[meqn*i+2] = 1000 /(gamma - 1);
    }
    if(xcell>=0.1 && xcell <0.9){
        d_q[meqn*i+2] = 0.01 /(gamma - 1);
    }
    if(xcell>=0.9){
        d_q[meqn*i+2] = 100 /(gamma - 1);
    }
}