n=20;
[x,t]=func1(n);
scatter(t, x);
%fac_n=fac(x, n);
outputs=[]

output=func2(x, n); % return y[n]
%%
for i=1:20
    outputs(i)=func2(x, i); % see all y[n] from n=1 to n=20
end
%%
B=[1, 0.5]
A=[1, -1.8*cos(3.14/16), 0.81]
filter_output=filter(B, A, x);

function [signal,timestamp]=func1(n)
    signal=[]
    timestamp=[];
    if n<0
        return 
    end    
    if n>20
        return
    end
    
    for i=1:n
        temp=(0.9)^i
        signal=[signal temp]
        timestamp=[timestamp i]
        %x[i]=signal
    end
end

function y=func2(x, n)
    fprintf(' n= %d ' ,n)
    fprintf(' x(n)=%d ',x(n) )
    if n<3
        fprintf(' n<3 ');        
        y=0;
    %elseif n<1
    %    x(n)=0
    %    y=0;
    else
        fprintf('  in resursion  \n') 
        y=1.8.*cos(3.14/16).*func2(x, n-1)-0.81.*func2(x, n-2)+x(n)+0.5.*x(n-1);
    end
end
function fn = fac(x, n)
    haha=x(n)
    n = floor(n);
    if (n > 1)
        fn = n * fac(x, n-1);
    else
        fn = 1;
    end
end
