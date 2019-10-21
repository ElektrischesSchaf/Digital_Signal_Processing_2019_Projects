n=20;
[x,t]=func1(n);
scatter(t, x);
output=func2(x, n);
%fac_n=fac(x, n);

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
    fprintf(' x(n)=%d',x(n) )
    if n<3
        fprintf(' n<2 \n')
        y=0;
    elseif n==0
        y=0;
    else
        fprintf(1, '  in resursion  ')
        fprintf('n= %d \n' ,n)
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
